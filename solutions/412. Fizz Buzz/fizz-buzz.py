class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      output_as_list = []
      
      for i in range(1, n + 1):
        output = ""

        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        if output == "": output += str(i)

        output_as_list.append(output)
    
      return output_as_list
