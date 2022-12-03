for (let i = 0; i < 100; i++) {
  if (i % 2 == 0) {
    continue
  }

  if (i > 10) {
    break
  }

  console.log(i)
}

let j = 0
while (true) {
  if (j === 20) {
    break
  }
  j++

  console.log(j)
}
