package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("now you have %g problems", math.Nextafter(2,3))
}
