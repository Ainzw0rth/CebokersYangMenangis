function whatNumber(num) {
  let ret;
  switch (num) {
    case 1:
      ret = 1;
      break;
    case 2:
      ret = 2;
      break;
    case 3:
      ret = 3;
      break;
    default:
      ret = "Below 1 or Above 3";
  }

  return ret;
}

console.log(whatNumber(0));
