class Password:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.__str__()


    def evaluate_strength(self) -> str:
        upper = lower = digits = symbols = 0
        special_chars = "!@#$%&_"

        for c in self.value:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
            elif c.isdigit():
                digits += 1
            elif c in special_chars:
                symbols += 1

        long_enough = len(self.value) > 8

        if upper >= 2 and lower >= 2 and digits >= 2 and symbols >= 2 and long_enough:
            return "\n Strong password."

        if upper < 2 and lower >= 2 and digits >= 2 and symbols >= 2 and long_enough:
            return "\n Fair password. Add at least one more uppercase letter to make it strong."

        feedback = ["\n Weak password. Please improve it:"]
        if upper < 2:
            feedback.append("- Add at least 2 uppercase letters")
        if lower < 2:
            feedback.append("- Add at least 2 lowercase letters")
        if digits < 2:
            feedback.append("- Add at least 2 digits")
        if symbols < 2:
            feedback.append("- Add at least 2 symbols (e.g. !@#...)")
        if not long_enough:
            feedback.append("- Password must be longer than 8 characters")

        return "\n".join(feedback)
