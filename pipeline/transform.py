import pandas as pd

MAX_UNIT_PRICE = 1000


def _flag(df, mask, reason):
    df.loc[mask & df["reject_reason"].isna(), "reject_reason"] = reason


def clean_orders(df):
    df = df.copy()
    df["reject_reason"] = None

    # Fixable problem: repair country names
    df["country"] = df["country"].str.strip().str.title()

    # Rule 1 - Completeness: customer ID is required
    _flag(
        df,
        df["customer_id"].isna(),
        "missing_customer_id"
    )

    # Rule 2 - Validity: date must be YYYY-MM-DD
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        format="%Y-%m-%d",
        errors="coerce"
    )
    _flag(
        df,
        df["order_date"].isna(),
        "invalid_date"
    )

    # Rule 3 - Validity: quantity must be positive
    _flag(
        df,
        ~(df["quantity"] > 0),
        "invalid_quantity"
    )

    # Rule 4 - Validity: price must be present, positive,
    # and at most MAX_UNIT_PRICE
    _flag(
        df,
        ~df["unit_price"].between(0.01, MAX_UNIT_PRICE),
        "invalid_unit_price"
    )

    # Rule 5 - Uniqueness: keep the first order_id
    _flag(
        df,
        df.duplicated("order_id", keep="first"),
        "duplicate_order_id"
    )

    # Separate rejected rows from clean rows
    rejected = df[df["reject_reason"].notna()].copy()

    clean = df[df["reject_reason"].isna()].drop(
        columns="reject_reason"
    ).copy()

    return clean, rejected


def revenue_by_country(clean):
    out = clean.assign(
        revenue=clean["quantity"] * clean["unit_price"]
    )

    out = out.groupby(
        "country",
        as_index=False
    )["revenue"].sum()

    out["revenue"] = out["revenue"].round(2)

    return out