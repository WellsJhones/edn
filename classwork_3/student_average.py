def main():
    try:
        # Read four grades with one decimal place
        n1, n2, n3, n4 = map(float, input("Enter four grades separated by space: ").split())

        # Calculate weighted average
        average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
        print(f"Average: {average:.1f}")

        # Decision based on average
            print(f"Exam score: {exam_score:.1f}")
            final_average = (average + exam_score) / 2
            if final_average >= 5.0:
                print("Student approved.")
            else:
                print("Student failed.")
            print(f"Final average: {final_average:.1f}")
    except ValueError:
        print("Please enter valid numeric grades.")

if __name__ == "__main__":
    main()
