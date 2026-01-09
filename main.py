import matplotlib.pyplot as plt
while True:
    print("\n1. Slope-Intercept Form")
    print("2. Intercept Form")
    print("3. Normal Form")
    print("4. Exit")
    ch = input("Select option: ")
    if ch == '4':
        break
    plt.figure(figsize=(8, 6))
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    x = np.linspace(-10, 10, 100)
    if ch == '1':
        m = float(input("Enter Slope (m): "))
        c = float(input("Enter Intercept (c): "))
        y = m * x + c
        plt.title(f"Slope Form: y = {m}x + {c}")
        plt.plot(x, y)
    elif ch == '2':
        a = float(input("Enter X-intercept (a): "))
        b = float(input("Enter Y-intercept (b): "))
        y = b * (1 - (x / a))
        plt.title(f"Intercept Form: x/{a} + y/{b} = 1")
        plt.plot(x, y)
    elif ch == '3':
        p = float(input("Enter Perpendicular Distance (p): "))
        w = float(input("Enter Angle (degrees): "))
        rad = np.deg2rad(w)
        y = (p - x * np.cos(rad)) / np.sin(rad)
        plt.title(f"Normal Form: p={p}, angle={w}")
        plt.plot(x, y)
    if input("Save graph as PNG? (y/n): ") == 'y':
        name = input("Enter filename: ")
        plt.savefig(f"{name}.png")
        print("Saved.")
    plt.show()
