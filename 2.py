TEST_DATA = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1],
             ['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1],
             ['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1],
             ['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1],
             ['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1],
             ['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]


def group_by_id_version(list_version):
    counts = {}

    for id, version in list_version:
        key = (id, version)
        counts[key] = counts.get(key, 0) + 1

    result = [[str(id), version, count] for (id, version), count in counts.items()]

    return result


res = group_by_id_version(TEST_DATA)
print(res)
