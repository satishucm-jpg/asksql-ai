def is_safe_sql(sql: str) -> bool:
    blocked_words = ["delete", "drop", "update", "insert", "alter", "truncate", "create"]

    sql_lower = sql.lower().strip()

    if not sql_lower.startswith("select"):
        return False

    for word in blocked_words:
        if word in sql_lower:
            return False

    return True