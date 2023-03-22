class Solution:
    def interpret(self, command: str) -> str:
        parsed_command = command
        commands = {
            "(al)": 'al',
            '()': 'o',
            'G': 'G',
        }

        for command, output in commands.items():
            parsed_command = parsed_command.replace(command, output)

        return parsed_command
