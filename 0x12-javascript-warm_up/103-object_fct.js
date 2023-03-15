#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
<<<<<<< HEAD
  myobject.value++;
=======
  myObject.value++;
>>>>>>> 41e3fcede37dfca2a3ccfaa9c7a51c613ff1cd67
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
