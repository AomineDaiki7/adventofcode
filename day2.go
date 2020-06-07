package main
import (
    "fmt"
    "io/ioutil"
    "strings"
    "strconv"
)

func main () {
    data, _ := ioutil.ReadFile("intcode_program")
    text := strings.Trim(string(data), "\n")
    input := strings.Split(text, ",")
    intcodes_input := make([]int, len(input))
    for i,element := range strings.Split(text, ",") {
        intcode, _ := strconv.Atoi(element)
        intcodes_input[i] = intcode
    }

    //Part 1
    intcodes := make([]int, len(intcodes_input))
    copy(intcodes, intcodes_input)
    intcodes[1] = 12
    intcodes[2] = 2
    output := intcode_computer(intcodes)
    fmt.Printf("Part 1, value at pos 0: %d\n",output[0])
    //Part 1 END
    
    //Part 2
    for noun := 0 ;noun < 100; noun++  {
        for verb := 0; verb < 100; verb++ {
            buffer := make([]int, len(intcodes_input))
            copy(buffer, intcodes_input)
            buffer[1] = noun
            buffer[2] = verb
            output := intcode_computer(buffer)
            if output[0] == 19690720 {
                fmt.Printf("Part2 answer: %d", 100 * noun + verb)
            }
        }
    }
    //Part-2 END.
}

func intcode_computer(intcodes []int) []int{
    var halt bool = false
    // i = instruction pointer.
    for i:=0;i < len(intcodes);{
        if ((i+2 > len(intcodes)) || halt ) {
            i += 4
        } else {
            opcode := intcodes[i]
            instruction_length := 0
            if opcode == 1 {
                instruction_length = 4
            } else if opcode == 2 {
                instruction_length = 4
            } else if opcode == 99 {
                instruction_length = 1
            } else {
                panic("panic: Unknown opcode")
            }
            intcodes, halt = run_opcode(intcodes[i:i+instruction_length], intcodes)
        i += instruction_length
    }
    }
    return intcodes
}

func run_opcode(instruction []int, intcodes []int) ([]int, bool){
    var halt bool = false
    if instruction[0] == 1 {
        param1 := instruction[1]
        param2 := instruction[2]
        intcodes[instruction[3]] = intcodes[param1] + intcodes[param2]
    }
    if instruction[0] == 2 {
        param1 := instruction[1]
        param2 := instruction[2]
        intcodes[instruction[3]] = intcodes[param1] * intcodes[param2]
    }
    if instruction[0] == 99 {
        halt = true
        return intcodes, halt
    }
    return intcodes, halt
}
