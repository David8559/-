"""Reconstruct an unweighted graph from a published all-pairs distance matrix."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "data" / "level4_b078_distance_matrix.csv"
EDGE_PATH = ROOT / "data" / "level4_b078_edges.csv"


def load_distance_matrix(path: Path = MATRIX_PATH) -> tuple[list[int], list[list[int]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [row for row in csv.reader(handle) if any(cell.strip() for cell in row)]
    nodes = [int(value) for value in rows[0][1:]]
    matrix: list[list[int]] = []
    for expected_node, row in zip(nodes, rows[1:], strict=True):
        if int(row[0]) != expected_node:
            raise ValueError(f"row label mismatch: expected {expected_node}, got {row[0]}")
        matrix.append([int(value) for value in row[1:]])
    if len(matrix) != len(nodes) or any(len(row) != len(nodes) for row in matrix):
        raise ValueError("distance matrix is not square")
    return nodes, matrix


def infer_edges(nodes: list[int], matrix: list[list[int]]) -> list[tuple[int, int]]:
    """For an unweighted simple graph, off-diagonal distance 1 means an edge."""
    return [
        (nodes[i], nodes[j])
        for i in range(len(nodes))
        for j in range(i + 1, len(nodes))
        if matrix[i][j] == 1
    ]


def floyd_warshall(nodes: list[int], edges: list[tuple[int, int]]) -> list[list[int]]:
    n = len(nodes)
    index = {node: i for i, node in enumerate(nodes)}
    infinity = n + 1
    distance = [[infinity] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    for left, right in edges:
        i, j = index[left], index[right]
        distance[i][j] = distance[j][i] = 1
    for k in range(n):
        for i in range(n):
            through_k = distance[i][k]
            for j in range(n):
                candidate = through_k + distance[k][j]
                if candidate < distance[i][j]:
                    distance[i][j] = candidate
    return distance


def validate(nodes: list[int], source: list[list[int]], edges: list[tuple[int, int]]) -> None:
    n = len(nodes)
    if any(source[i][i] != 0 for i in range(n)):
        raise ValueError("non-zero diagonal")
    if any(source[i][j] != source[j][i] for i in range(n) for j in range(n)):
        raise ValueError("matrix is not symmetric")
    reconstructed = floyd_warshall(nodes, edges)
    mismatches = [
        (nodes[i], nodes[j], source[i][j], reconstructed[i][j])
        for i in range(n)
        for j in range(n)
        if source[i][j] != reconstructed[i][j]
    ]
    if mismatches:
        raise ValueError(f"distance closure failed; first mismatches: {mismatches[:5]}")


def write_edges(edges: list[tuple[int, int]], path: Path = EDGE_PATH) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["source", "target", "weight", "provenance"])
        writer.writerows((left, right, 1, "B078-distance-equals-1") for left, right in edges)


def main() -> None:
    nodes, matrix = load_distance_matrix()
    edges = infer_edges(nodes, matrix)
    validate(nodes, matrix, edges)
    write_edges(edges)
    print(f"PASS: B078 level 4 has {len(nodes)} nodes and {len(edges)} undirected edges; all distances match.")


if __name__ == "__main__":
    main()
