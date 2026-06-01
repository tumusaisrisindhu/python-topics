import copy


class CopySimulator:

    def run(self):

        original = [
            ["Python", "Java"],
            ["React", "Angular"]
        ]

        assigned = original

        shallow = copy.copy(original)

        deep = copy.deepcopy(original)

        print("\n========== BEFORE CHANGES ==========\n")

        self.display(original, assigned, shallow, deep)

        shallow[0].append("Django")

        deep[1].append("Vue")

        print("\n========== AFTER CHANGES ==========\n")

        self.display(original, assigned, shallow, deep)

    def display(self, original, assigned, shallow, deep):

        print("ORIGINAL")
        print(original)
        print("ID:", id(original))
        print()

        print("ASSIGNED")
        print(assigned)
        print("ID:", id(assigned))
        print()

        print("SHALLOW")
        print(shallow)
        print("ID:", id(shallow))
        print()

        print("DEEP")
        print(deep)
        print("ID:", id(deep))
        print()