#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <iomanip>
#include <algorithm>

class Ingredient
{
public:
    std::string name;
    double calories, protein, fats, carbs;

    Ingredient(std::string name, double calories, double protein, double fats, double carbs)
        : name(name), calories(calories), protein(protein), fats(fats), carbs(carbs) {}

    void print() const
    {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << name << " (Calories: " << calories << ", Protein: " << protein
                  << ", Fats: " << fats << ", Carbs: " << carbs << ")";
    }
};

class Dish
{
public:
    std::string name;
    std::vector<Ingredient> ingredients;
    std::map<std::string, int> quantities;

    Dish(std::string name) : name(name) {}

    void addIngredient(const Ingredient &ingredient, int quantity)
    {
        ingredients.push_back(ingredient);
        quantities[ingredient.name] = quantity;
    }

    double getTotalCalories() const
    {
        double totalCalories = 0;
        for (const auto &ingredient : ingredients)
        {
            auto it = quantities.find(ingredient.name);
            if (it != quantities.end())
            {
                int quantity = it->second;
                totalCalories += (ingredient.calories * quantity / 100.0);
            }
        }
        return totalCalories;
    }

    void printDescription() const
    {
        std::cout << name << " contains:\n";
        for (const auto &ingredient : ingredients)
        {
            auto it = quantities.find(ingredient.name);
            if (it != quantities.end())
            {
                int quantity = it->second;
                std::cout << ingredient.name << ": " << quantity << " grams\n";
            }
        }
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Total Calories: " << getTotalCalories() << "\n";
    }
};

class Day
{
public:
    std::string date;
    std::vector<Dish> dishes;

    Day(std::string date) : date(date) {}

    void addDish(const Dish &dish)
    {
        dishes.push_back(dish);
    }

    double getTotalCalories() const
    {
        double totalCalories = 0;
        for (const auto &dish : dishes)
        {
            totalCalories += dish.getTotalCalories();
        }
        return totalCalories;
    }

    void printDailySummary() const
    {
        std::cout << "Date: " << date << "\n";
        for (const auto &dish : dishes)
        {
            dish.printDescription();
            std::cout << "\n";
        }
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Total Calories for the Day: " << getTotalCalories() << "\n";
    }
};

class CalorieTracker
{
private:
    static std::vector<Ingredient> ingredients;
    static std::vector<Dish> dishes;
    static std::vector<Day> days;

    static void addIngredient()
    {
        std::string name;
        double calories, protein, fats, carbs;

        std::cout << "Enter ingredient name: ";
        std::cin.ignore();
        std::getline(std::cin, name);
        std::cout << "Enter calories per 100g: ";
        std::cin >> calories;
        std::cout << "Enter protein per 100g: ";
        std::cin >> protein;
        std::cout << "Enter fats per 100g: ";
        std::cin >> fats;
        std::cout << "Enter carbs per 100g: ";
        std::cin >> carbs;

        ingredients.emplace_back(name, calories, protein, fats, carbs);
        std::cout << "Ingredient added successfully!" << std::endl;
    }

    static void addDish()
    {
        std::string name;
        std::cout << "Enter dish name: ";
        std::cin.ignore();
        std::getline(std::cin, name);
        Dish dish(name);

        while (true)
        {
            std::string ingredientName;
            std::cout << "Enter ingredient name (or 'done' to finish): ";
            std::getline(std::cin, ingredientName);
            if (ingredientName == "done")
                break;

            auto ingredient = findIngredientByName(ingredientName);
            if (ingredient == nullptr)
            {
                std::cout << "Ingredient not found. Please add it first." << std::endl;
                continue;
            }

            int quantity;
            std::cout << "Enter quantity in grams: ";
            std::cin >> quantity;
            std::cin.ignore();

            dish.addIngredient(*ingredient, quantity);
        }
        dishes.push_back(dish);
        std::cout << "Dish added successfully!" << std::endl;
    }

    static void addDishToDay()
    {
        std::string date;
        std::cout << "Enter date (YYYY-MM-DD): ";
        std::cin >> date;
        auto day = findDayByDate(date);
        if (day == nullptr)
        {
            days.emplace_back(date);
            day = &days.back();
        }

        std::string dishName;
        std::cout << "Enter dish name: ";
        std::cin.ignore();
        std::getline(std::cin, dishName);
        auto dish = findDishByName(dishName);
        if (dish == nullptr)
        {
            std::cout << "Dish not found. Please add it first." << std::endl;
            return;
        }

        day->addDish(*dish);
        std::cout << "Dish added to day successfully!" << std::endl;
    }

    static void viewDaySummary()
    {
        std::string date;
        std::cout << "Enter date (YYYY-MM-DD): ";
        std::cin >> date;
        auto day = findDayByDate(date);
        if (day == nullptr)
        {
            std::cout << "No records found for this date." << std::endl;
            return;
        }
        day->printDailySummary();
    }

    static Ingredient *findIngredientByName(const std::string &name)
    {
        auto it = std::find_if(ingredients.begin(), ingredients.end(),
                               [&name](const Ingredient &i)
                               { return i.name == name; });
        return it != ingredients.end() ? &(*it) : nullptr;
    }

    static Dish *findDishByName(const std::string &name)
    {
        auto it = std::find_if(dishes.begin(), dishes.end(),
                               [&name](const Dish &d)
                               { return d.name == name; });
        return it != dishes.end() ? &(*it) : nullptr;
    }

    static Day *findDayByDate(const std::string &date)
    {
        auto it = std::find_if(days.begin(), days.end(),
                               [&date](const Day &d)
                               { return d.date == date; });
        return it != days.end() ? &(*it) : nullptr;
    }

public:
    static void run()
    {
        while (true)
        {
            std::cout << "\nCalorie Tracker Menu:" << std::endl;
            std::cout << "1. Add Ingredient" << std::endl;
            std::cout << "2. Add Dish" << std::endl;
            std::cout << "3. Add Dish to Day" << std::endl;
            std::cout << "4. View Day Summary" << std::endl;
            std::cout << "5. Exit" << std::endl;
            std::cout << "Choose an option: ";

            int choice;
            std::cin >> choice;

            switch (choice)
            {
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
                std::cout << "Exiting..." << std::endl;
                return;
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
            }
        }
    }
};

std::vector<Ingredient> CalorieTracker::ingredients;
std::vector<Dish> CalorieTracker::dishes;
std::vector<Day> CalorieTracker::days;

int main()
{
    CalorieTracker::run();
    return 0;
}