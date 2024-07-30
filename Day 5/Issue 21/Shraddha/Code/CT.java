import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

public class CT {
    private List<Ingredient> ingredientList;
    private List<Dish> dishList;
    private List<Day> dayList;

    public CT() {
        this.ingredientList = new ArrayList<>();
        this.dishList = new ArrayList<>();
        this.dayList = new ArrayList<>();
    }

    public void addIngredient(String name, double fat, double calories, double protein) {
        ingredientList.add(new Ingredient(name, fat, calories, protein));
    }

    public void createDish(String name) {
        dishList.add(new Dish(name));
    }

    public void addIngredientToDish(String dishName, String ingredientName, double quantity) {
        Dish dish = findDishByName(dishName);
        Ingredient ingredient = findIngredientByName(ingredientName);
        if (dish != null && ingredient != null) {
            dish.addIngredient(ingredient, quantity);
        }
    }

    public void addDishToDay(Date date, String dishName, double quantity) {
        Day day = findDayByDate(date);
        Dish dish = findDishByName(dishName);
        if (day == null) {
            day = new Day(date);
            dayList.add(day);
        }
        if (dish != null) {
            day.addDish(dish, quantity);
        }
    }

    public void displayTotalCaloriesForDay(Date date) {
        Day day = findDayByDate(date);
        if (day != null) {
            System.out.println("Total calories for " + date + ": " + day.calculateTotalCalories());
        } else {
            System.out.println("No records found for " + date);
        }
    }

    private Ingredient findIngredientByName(String name) {
        for (Ingredient ingredient : ingredientList) {
            if (ingredient.getName().equalsIgnoreCase(name)) {
                return ingredient;
            }
        }
        return null;
    }

    private Dish findDishByName(String name) {
        for (Dish dish : dishList) {
            if (dish.getName().equalsIgnoreCase(name)) {
                return dish;
            }
        }
        return null;
    }

    private Day findDayByDate(Date date) {
        for (Day day : dayList) {
            if (day.getDate().equals(date)) {
                return day;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CT tracker = new CT();

        while (true) {
            System.out.println("1. Add Ingredient");
            System.out.println("2. Create Dish");
            System.out.println("3. Add Ingredient to Dish");
            System.out.println("4. Add Dish to Day");
            System.out.println("5. Display Total Calories for Day");
            System.out.println("6. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.println("Enter ingredient name:");
                    String ingredientName = scanner.nextLine();
                    System.out.println("Enter fat:");
                    double fat = scanner.nextDouble();
                    System.out.println("Enter calories:");
                    double calories = scanner.nextDouble();
                    System.out.println("Enter protein:");
                    double protein = scanner.nextDouble();
                    tracker.addIngredient(ingredientName, fat, calories, protein);
                    break;
                case 2:
                    System.out.println("Enter dish name:");
                    String dishName = scanner.nextLine();
                    tracker.createDish(dishName);
                    break;
                case 3:
                    System.out.println("Enter dish name:");
                    String dishNameForIngredient = scanner.nextLine();
                    System.out.println("Enter ingredient name:");
                    String ingredientNameForDish = scanner.nextLine();
                    System.out.println("Enter quantity:");
                    double ingredientQuantity = scanner.nextDouble();
                    tracker.addIngredientToDish(dishNameForIngredient, ingredientNameForDish, ingredientQuantity);
                    break;
                case 4:
                    System.out.println("Enter date (yyyy-mm-dd):");
                    String dateStr = scanner.nextLine();
                    Date date = java.sql.Date.valueOf(dateStr);
                    System.out.println("Enter dish name:");
                    String dishNameForDay = scanner.nextLine();
                    System.out.println("Enter quantity:");
                    double dishQuantity = scanner.nextDouble();
                    tracker.addDishToDay(date, dishNameForDay, dishQuantity);
                    break;
                case 5:
                    System.out.println("Enter date (yyyy-mm-dd):");
                    String displayDateStr = scanner.nextLine();
                    Date displayDate = java.sql.Date.valueOf(displayDateStr);
                    tracker.displayTotalCaloriesForDay(displayDate);
                    break;
                case 6:
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Try again.");
                    break;
            }
        }
    }
}
