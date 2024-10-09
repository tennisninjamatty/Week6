def get_keys_by_value(d: dict, target_value: int) -> list:
    keys = []
    for key, value in d.items():
        if value == target_value:
            keys.append(key)
        else:
            keys = []
    return keys


some_dictionary = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 5}
print(get_keys_by_value(some_dictionary, 1))
