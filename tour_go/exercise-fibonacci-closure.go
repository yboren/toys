package main

import "fmt"

func fibonacci() func(int) int {
	last1 := 0
	last2 := 1
	return func(x int) int {
		last1, last2 = last2, last1+last2
		return last2
	}

}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f(i))
	}
}
