"""cpmp which performs copies because memory values are positive"""

def mem_addr(i):
    return 0x10010000 + i * 4

initial_registers = {
    11: 123,
    12: 100,
    13: mem_addr(2),
    14: mem_addr(3),
}

instructions = [
    "cpmp\t$11, $13, $12",
    "cpmp\t$14, $14, $12",
]

modified_registers = {
    11: 100,
    14: 100,
}

initial_memory = {
    2: 10,
    3: 20,
}
