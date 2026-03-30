import math, random, os
from cesta_k_suboru import check_leaf_depth, check_left_align,
                           check_min, build_min_tree, draw_tree

"""
Nezabudnite napisat realnu cestu k suboru v importe.

Na vykreslenie stromu pouzite napr.
    dot -Tpng 07_failed_trees\\tree_xyz.dot -o tree.png
Pozor, musite mat nainstalovany program dot.

Ak nefunguje os.makedir, rucne vytvorte adresar '07_failed_trees' a
nastavte si ho ako bezny (z kade budete spustat program).
"""

DEPTH_FAILED = 0
ALIGN_FAILED = 1
MIN_FAILED = 2

TREE_1 = BinTree(Node(1, Node(2, Node(2), Node(3)), Node(1, Node(1), None)))
TREE_2 = BinTree(Node(1, Node(1, Node(2, Node(2), Node(3)),
                                 Node(1, Node(1), Node(4))),
                         Node(3, Node(3, Node(3), Node(5)), None)))
TREE_3 = BinTree(Node(1, Node(2, Node(2), Node(3)), Node(1)))
TREE_4 = BinTree(Node(1, Node(2, Node(2), Node(3)), Node(1, None, Node(1))))
TREE_5 = BinTree(Node(1, Node(2, Node(2), None), Node(1, Node(1), None)))
TREE_6 = BinTree(Node(1, Node(2, Node(2), Node(3)), Node(0, Node(1), None)))


def test_check_leaf_depth(tree: BinTree,
                          expect: bool) -> None | tuple[bool, bool]:
    got = check_leaf_depth(tree)
    return None if expect == got else (expect, got)


def test_check_left_align(tree: BinTree,
                          expect: bool) -> None | tuple[bool, bool]:
    got = check_left_align(tree)
    return None if expect == got else (expect, got)


def test_check_min(tree: BinTree,
                   expect: bool) -> None | tuple[bool, bool]:
    got = check_min(tree)
    return None if expect == got else (expect, got)


def test_build_min_tree(leaves: list[int]) -> None | tuple[BinTree, int]:
    tree = build_min_tree(leaves)
    if not check_leaf_depth(tree):
        return (tree, DEPTH_FAILED)
    if not check_left_align(tree):
        return (tree, ALIGN_FAILED)
    if not check_min(tree):
        return (tree, MIN_FAILED)
    return None


def generate_bmt_testcases(testcases: list[list[int]]) -> None:
    leaves = []
    testcases.append(leaves.copy())
    for _ in range(20):
        leaves.append(random.randint(-50, 50))
        testcases.append(leaves.copy())
        for _ in range(20):
            leaves.append(random.randint(-50, 50))
            testcases.append(leaves.copy())
            leaves.pop()


def testing_check_leaf_depth() -> tuple[int, int]:
    passed, total = 0, 0
    testcases = [
        (TREE_1, True),
        (TREE_2, True),
        (TREE_3, False)
    ]

    for i, (tree, expect) in enumerate(testcases):
        res = test_check_leaf_depth(tree, expect)
        if res is None:
            print(f"check_leaf_depth test {i + 1}: PASSED")
            passed += 1
        else:
            expected, got = res
            print(f"check_leaf_depth test {i + 1}: FAILED")
            print(f"\t> expected: {expected}, but got: {got}")
        total += 1

    print(f"check_leaf_depth tests: passed: {passed}, failed: {total - passed}, total: {total}")
    return passed, total


def testing_check_left_align() -> tuple[int, int]:
    passed, total = 0, 0
    testcases = [
        (TREE_1, True),
        (TREE_2, True),
        (TREE_4, False),
        (TREE_5, False)
    ]

    for i, (tree, expect) in enumerate(testcases):
        res = test_check_left_align(tree, expect)
        if res is None:
            print(f"check_left_align test {i + 1}: PASSED")
            passed += 1
        else:
            expected, got = res
            print(f"check_left_align test {i + 1}: FAILED")
            print(f"\t> expected: {expected}, but got: {got}")
        total += 1

    print(f"check_left_align tests: passed: {passed}, failed: {total - passed}, total: {total}")
    return passed, total


def testing_check_min() -> tuple[int, int]:
    passed, total = 0, 0
    testcases = [
        (TREE_1, True),
        (TREE_2, True),
        (TREE_6, False)
    ]

    for i, (tree, expect) in enumerate(testcases):
        res = test_check_min(tree, expect)
        if res is None:
            print(f"check_min test {i + 1}: PASSED")
            passed += 1
        else:
            expected, got = res
            print(f"check_min test {i + 1}: FAILED")
            print(f"\t> expected: {expected}, but got: {got}")
        total += 1

    print(f"check_min tests: passed: {passed}, failed: {total - passed}, total: {total}")
    return passed, total


def testing_build_min_tree(failed: list[int, BinTree]) -> tuple[int, int]:
    passed, total = 0, 0
    testcases = [
        [2, 3, 1],
        [2, 3, 1, 4, 3, 5]
    ]
    generate_bmt_testcases(testcases)

    for i, leaves in enumerate(testcases):
        res = test_build_min_tree(leaves)
        if res is None:
            print(f"build_min_tree test {i + 1}: PASSED")
            passed += 1
        else:
            tree, f_code = res
            f_msg = "incorrect depth" if f_code == DEPTH_FAILED \
                    else ("incorrect align" if f_code == ALIGN_FAILED \
                          else "incorrect min")
            print(f"build_min_tree test {i + 1}: FAILED")
            print(f"\t> leaves: {leaves}")
            print(f"\t> reason: {f_msg}, filename: tree_{i + 1}")
            failed.append((i, tree))
        total += 1

    print(f"build_min_tree tests: passed: {passed}, failed: {total - passed}, total: {total}")
    return passed, total


def testing() -> None:
    passed, total = 0, 0

    p_res, t_res = testing_check_leaf_depth()
    if (p_res != t_res):
        print("check_leaf_depth testing FAILED")
        print("ABORTING testing ..")
        return
    passed += p_res
    total += t_res
    print()

    p_res, t_res = testing_check_left_align()
    if (p_res != t_res):
        print("check_left_align testing FAILED")
        print("ABORTING testing ..")
        return
    passed += p_res
    total += t_res
    print()

    p_res, t_res = testing_check_min()
    if (p_res != t_res):
        print("check_min testing FAILED")
        print("ABORTING testing ..")
        return
    passed += p_res
    total += t_res
    print()

    failed_trees = []
    p_res, t_res = testing_build_min_tree(failed_trees)
    passed += p_res
    total += t_res

    print(f"total tests: passed: {passed}, failed: {total - passed}, total: {total}")

    if (p_res != t_res):
        ch = input("Do you wish to see the failed trees? [Y/...]: ")
        if ch.lower() == "y":
            os.makedirs("07_failed_trees", exist_ok = True)
            for (i, tree) in failed_trees:
                draw_tree(tree, f"07_failed_trees\\tree_{i + 1}.dot")


testing()
