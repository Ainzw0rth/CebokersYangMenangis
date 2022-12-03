try {
  let a = 1;
  if (a == 1) {
    throw "Error";
  }
  console.log("Do something");
} catch (e) {
  console.log(e);
} finally {
  console.log("Finally");
}
