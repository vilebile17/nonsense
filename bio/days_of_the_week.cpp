/*
This week's question is as follows:
- I give you a date (dd/mm/yyyy) format
- give me what day of the week it was
- NO DATE AND TIME LIBRARIES!!!
ok go do it, bye
*/

#include <iostream>
#include <string>

int cool_func() { return 0; }

int main() {
    std::string full_date;
    std::cin >> full_date;

    if (full_date.size() != 10 * sizeof(char)) {
        std::cout << "Invalid date format! (We want DD/MM/YYYY)\n";
        return 1;
    }

    int date = std::stoi(full_date.substr(0, 2));
    int month = std::stoi(full_date.substr(3, 2));
    int year = std::stoi(full_date.substr(6, 4));

    // calculating the number of days since 01/01/0001 (including that date)
    // We begin by simply adding all of the days from 0001 to the year before
    // by first assuming no leap years
    int num_days_since_beginning = (year - 1) * 365;

    // Then we add a day for every year which is a multiple of four, but remove
    // it if it's also a multiple of 100
    num_days_since_beginning += ((year - 1) / 4) - ((year - 1) / 100);
    // BUT, we need to add that back if the year is a multiple of 400;
    // that's the classic procedure for the Gregorian Calendar
    num_days_since_beginning += (year - 1) / 400;

    bool is_leap_year =
        ((year % 4 == 0) && (year % 100 == 0) == (year % 400 == 0));

    if (month <= 2) {
        // If the day is in Jan or Feb it's nice and easy: simply add the date
        // for Jan and if Feb then all of the days in Jan (31) + date
        num_days_since_beginning += (month - 1) * 31 + date;
    } else if (month >= 3 && month <= 7) {
        // This one is a bit confusing:
        // - First we add all of the days in Jan + Feb
        // - We add an extra day to Feb if it's a leap-year
        // - Then we add 30 for the other full months that have passed in the
        // year
        // - Then we add and extra day for each month that has passed with 31
        // days
        // - Finally we add the date
        num_days_since_beginning +=
            59 + is_leap_year + (month - 3) * 30 + (month - 2) / 2 + date;
    } else {
        // This one has a similar idea to the above...
        num_days_since_beginning +=
            212 + is_leap_year + (month - 8) * 30 + (month - 7) / 2 + date;
    }

    // 01/01/0001 was a Monday; Seven days later was also a Monday: the days of
    // the week loop every seven days
    // (Can I win a Nobel Prize for that revolutionary discovery??)
    // We just take the mod 7 of the number of days and get the day-name from an
    // array
    std::string days[7] = {"Sunday",   "Monday", "Tuesday", "Wednesday",
                           "Thursday", "Friday", "Saturday"};
    std::cout << days[num_days_since_beginning % 7] << "\n";
    return 0;
}
