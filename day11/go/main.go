package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
)

func recurse(input []int, curr int) {

}

func change(input []int) []int {
    if len(input) >= 10000 {
        part1 := input[:len(input) / 2] 
        part2 := input[len(input) / 2:] 

        var wg sync.WaitGroup

        wg.Add(2)
        go func() {
            defer wg.Done()
            part1 = change(part1)
        }()

        go func() {
            defer wg.Done()
            part2 = change(part2)
        }()

        wg.Wait()
        return append(part1, part2...)
    }
    process := func(part []int) []int { 
        new_order := make([]int, 0)
        for _, n := range part {
            if n == 0 {
                new_order = append(new_order, 1)
            } else if len(strconv.Itoa(n)) % 2 == 0 {
                str := strconv.Itoa(n)
                n1, _ := strconv.Atoi(str[:len(str) / 2])
                n2, _ := strconv.Atoi(str[len(str) / 2:])
                new_order = append(new_order, n1)
                new_order = append(new_order, n2)
            } else {
                new_order = append(new_order, n * 2024)
            }
        }
        return new_order
    }
    return process(input)
}

func main() {
    dat, err := os.ReadFile("./input")
    if err != nil {
        fmt.Println("v%", err)
    }

    input := make([]int, 0)
    s := strings.TrimSpace(string(dat))
    split := strings.Split(s, " ")
    for _, c := range split {
        cInt, err := strconv.Atoi(c)
        if err != nil {
            continue
        }
        input = append(input, cInt) 
    }

    N := 75
    for range N {
        input = change(input)
        fmt.Println(len(input))
    }
}

