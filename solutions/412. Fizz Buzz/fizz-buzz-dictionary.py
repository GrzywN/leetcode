class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      output_as_list = []
      outputs_based_on_divisibility = {
        3: "Fizz",
        5: "Buzz"
      }

      for i in range(1, n + 1):
        output = ""

        for divider in outputs_based_on_divisibility:
          if i % divider == 0:
            output += outputs_based_on_divisibility[divider]

        if output == "": output += str(i)

        output_as_list.append(output)
    
      return output_as_list
