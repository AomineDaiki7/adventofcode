package main

import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func main() {
    data, err := ioutil.ReadFile("./puzzle1_input.txt")
    if err != nil {
        panic(err)
    }
    text := string(data)
    modules := strings.Split(text, "\n")
    fuel_map := make(map[string]int)
    for _, module := range modules {
        val, _ := strconv.Atoi(module)
        fuel_map[module] = calculate_fuel(val)
    }

    // Part 1 calculate total fuel for all modules.
    total_fuel := 0
    for _, fuel := range fuel_map {
        total_fuel +=fuel
    }
    fmt.Printf("Part1 := Total fuel required: %d \n", total_fuel)

    total_fuel = 0

    // Part 2 calculate total fuel with fuel required for fuel.
    for _, fuel := range fuel_map {
            total_fuel += fuel_for_fuel(fuel)
        }
    fmt.Printf("Part2 := Total fuel = %d \n", total_fuel)
}

func calculate_fuel(module int) int {
    fuel := (module/3)-2
    if fuel < 0 {
        fuel = 0
    }
    return fuel
}

func fuel_for_fuel(fuel int) int {
    _fuel_for_fuel := fuel
    for fuel > 0 {
        fuel = calculate_fuel(fuel)
        if fuel > 0 {
            _fuel_for_fuel += fuel
        }
    }
    return _fuel_for_fuel
}
