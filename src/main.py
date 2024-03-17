import input
import output
import visualizer

def main():
    output.displayMenu()
    choice = input.getChoice()
    
    if choice == 1 or choice == 2:
        if choice == 1:
            curve_method = 'Brute Force'
        elif choice == 2:
            curve_method = 'Divide and Conquer'
        else:
            raise ValueError("Jenis kurva tidak valid.")        
        visualizer.plot_curve(curve_method)
        
    elif choice == 3: # Membandingkan 2 Algoritma
        points, iterations = input.getInputQuadratic()
        elapsed_time_bf = output.calculateElapsedTime(points, iterations, 'Brute Force')
        elapsed_time_dnc = output.calculateElapsedTime(points, iterations, 'Divide and Conquer')
        output.displayComparison(elapsed_time_bf, elapsed_time_dnc)
        output.displayTotalPoints(iterations)
        
    elif choice == 4:
        # Handle Multi Bézier Curve
        pass
    
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
