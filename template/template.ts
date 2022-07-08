import * as readline from 'readline';

let alphabetLowerCase:string = "abcdefghijklmnopqrstuvwxyz";
console.log(alphabetLowerCase.length)
let alphabetUpperCase:string = alphabetLowerCase.toUpperCase()
console.log(alphabetUpperCase.length)

let number: string = "1234567890"
console.log(number.length)

let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let email: any = rl.question("What's your email?",(answer1) => {
  if (answer1 != ("@" && ".com")) {
    return console.log("Invalid Email");
  }
  rl.close()
});

let password: any = rl.question("What's your password", (answer2) => {
  if (answer2.length < 8) {
    return console.log("Invalid Password")
  }
})