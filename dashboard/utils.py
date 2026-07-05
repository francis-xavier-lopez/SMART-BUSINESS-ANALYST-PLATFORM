def detect_columns(df):
    """
    Automatically detect important business columns
    based on common column names.
    """

    # Convert all column names to lowercase and remove extra spaces
    columns = {col.lower().strip(): col for col in df.columns}

    keywords = {
        "revenue": [
            "revenue",
            "amount",
            "sales amount",
            "income",
            "net amount",
            "total amount",
            "price"
        ],

        "sales": [
            "sales",
            "quantity",
            "qty",
            "units",
            "sold"
        ],

        "product": [
            "product",
            "product name",
            "item",
            "item name"
        ],

        "date": [
            "date",
            "order date",
            "invoice date",
            "purchase date"
        ],

        "category": [
            "category",
            "product category",
            "department",
            "segment",
            "type"
        ]
    }

    detected = {}

    for field, possible_names in keywords.items():
        detected[field] = None

        for keyword in possible_names:
            if keyword in columns:
                detected[field] = columns[keyword]
                break

    return detected