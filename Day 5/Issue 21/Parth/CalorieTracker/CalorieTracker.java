import java.util.*;

class Ingredient {
    String name;
    double calories;
    double protein;
    double fats;
    double carbs;

    public Ingredient(String name, double calories, double protein, double fats, double carbs) {
        this.name = name;
        this.calories = calories;
        this.protein = protein;
        this.fats = fats;
        this.carbs = carbs;
    }

    @Override
    public String toString() {
        return String.format("%s (Calories: %.2f, Protein: %.2f, Fats: %.2f, Carbs: %.2f)", 
                             name, calories, protein, fats, carbs);
    }
}

class Dish {
    String name;
    List<Ingredient> ingredients;
    Map<Ingredient, Integer> quantities; // Ingredient and quantity in grams

    public Dish(String name) {
        this.name = name;
        this.ingredients = new ArrayList<>();
        this.quantities = new HashMap<>();
    }

    public void addIngredient(Ingredient ingredient, int quantity) {
        ingredients.add(ingredient);
        quantities.put(ingredient, quantity);
    }

    public double getTotalCalories() {
        double totalCalories = 0;
        for (Ingredient ingredient : ingredients) {
            int quantity = quantities.get(ingredient);
            totalCalories += (ingredient.calories * quantity / 100.0);
        }
        return totalCalories;
    }

    public String getDescription() {
        StringBuilder description = new StringBuilder(name + " contains:\n");
        for (Ingredient ingredient : ingredients) {
            int quantity = quantities.get(ingredient);
            description.append(String.format("%s: %d grams\n", ingredient.name, quantity));
        }
        description.append(String.format("Total Calories: %.2f\n", getTotalCalories()));
        return description.toString();
    }
}

class Day {
    String date;
    List<Dish> dishes;

    public Day(String date) {
        this.date = date;
        this.dishes = new ArrayList<>();
    }

    public void addDish(Dish dish) {
        dishes.add(dish);
    }

    public double getTotalCalories() {
        double totalCalories = 0;
        for (Dish dish : dishes) {
            totalCalories += dish.getTotalCalories();
        }
        return totalCalories;
    }

    public String getDailySummary() {
        StringBuilder summary = new StringBuilder("Date: " + date + "\n");
        for (Dish dish : dishes) {
            summary.append(dish.getDescription()).append("\n");
        }
        summary.append(String.format("Total Calories for the Day: %.2f\n", getTotalCalories()));
        return summary.toString();
    }
}

public class CalorieTracker {
    static Scanner scanner = new Scanner(System.in);
    static List<Ingredient> ingredients = new ArrayList<>();
    static List<Dish> dishes = new ArrayList<>();
    static List<Day> days = new ArrayList<>();

    public static void main(String[] args) {
        while (true) {
            System.out.println("\nCalorie Tracker Menu:");
            System.out.println("1. Add Ingredient");
            System.out.println("2. Add Dish");
            System.out.println("3. Add Dish to Day");
            System.out.println("4. View Day Summary");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    addIngredient();
                    break;
                case 2:
                    addDish();
                    break;
                case 3:
                    addDishToDay();
                    break;
                case 4:
                    viewDaySummary();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addIngredient() {
        System.out.print("Enter ingredient name: ");
        String name = scanner.nextLine();
        System.out.print("Enter calories per 100g: ");
        double calories = scanner.nextDouble();
        System.out.print("Enter protein per 100g: ");
        double protein = scanner.nextDouble();
        System.out.print("Enter fats per 100g: ");
        double fats = scanner.nextDouble();
        System.out.print("Enter carbs per 100g: ");
        double carbs = scanner.nextDouble();
        scanner.nextLine(); // consume newline

        Ingredient ingredient = new Ingredient(name, calories, protein, fats, carbs);
        ingredients.add(ingredient);
        System.out.println("Ingredient added successfully!");
    }

    private static void addDish() {
        System.out.print("Enter dish name: ");
        String name = scanner.nextLine();
        Dish dish = new Dish(name);

        while (true) {
            System.out.print("Enter ingredient name (or 'done' to finish): ");
            String ingredientName = scanner.nextLine();
            if (ingredientName.equalsIgnoreCase("done")) break;

            Ingredient ingredient = findIngredientByName(ingredientName);
            if (ingredient == null) {
                System.out.println("Ingredient not found. Please add it first.");
                continue;
            }

            System.out.print("Enter quantity in grams: ");
            int quantity = scanner.nextInt();
            scanner.nextLine(); // consume newline

            dish.addIngredient(ingredient, quantity);
        }
        dishes.add(dish);
        System.out.println("Dish added successfully!");
    }

    private static void addDishToDay() {
        System.out.print("Enter date (YYYY-MM-DD): ");
        String date = scanner.nextLine();
        Day day = findDayByDate(date);
        if (day == null) {
            day = new Day(date);
            days.add(day);
        }

        System.out.print("Enter dish name: ");
        String dishName = scanner.nextLine();
        Dish dish = findDishByName(dishName);
        if (dish == null) {
            System.out.println("Dish not found. Please add it first.");
            return;
        }

        day.addDish(dish);
        System.out.println("Dish added to day successfully!");
    }

    private static void viewDaySummary() {
        System.out.print("Enter date (YYYY-MM-DD): ");
        String date = scanner.nextLine();
        Day day = findDayByDate(date);
        if (day == null) {
            System.out.println("No records found for this date.");
            return;
        }
        System.out.println(day.getDailySummary());
    }

    private static Ingredient findIngredientByName(String name) {
        for (Ingredient ingredient : ingredients) {
            if (ingredient.name.equalsIgnoreCase(name)) {
                return ingredient;
            }
        }
        return null;
    }

    private static Dish findDishByName(String name) {
        for (Dish dish : dishes) {
            if (dish.name.equalsIgnoreCase(name)) {
                return dish;
            }
        }
        return null;
    }

    private static Day findDayByDate(String date) {
        for (Day day : days) {
            if (day.date.equals(date)) {
                return day;
            }
        }
        return null;
    }
}