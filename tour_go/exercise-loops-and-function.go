package main

import (
	"fmt"
)

func Sqrt(x float64) float64 {
	z := 1.0
	for i := 1; i <= 10; i++ {
		z = z - ( z*z - x ) / (2*x)
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(3))
	fmt.Println(Sqrt(4))
	fmt.Println(Sqrt(10))
}
