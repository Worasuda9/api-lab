# api-lab

| Characteristic | Block | Value in the test | Test covering the block |
| -------- | -------- | -------- | -------- |
| C1 Value of stars | below 1 | 0 | `test_stars_out_of_range[below-1]` |
| C1 Value of stars | 1 to 5 (base) | 3 | `test_base_choice_is_saved` |
| C1 Value of stars | above 5 | 6 | `test_stars_out_of_range[above-5]` |
| C2 Type of stars | whole number (base) | 3 | `test_base_choice_is_saved` |
| C2 Type of stars | decimal | 3.5 | `test_decimal_stars_are_refused` |
| C2 Type of stars | text | "3" | `test_text_stars_are_refused` |
| C2 Type of stars | missing | no field | `test_missing_stars_are_refused` |
| C3 Pizza | exists (base) | a new pizza | `test_base_choice_is_saved` |
| C3 Pizza | does not exist | 999999999 | `test_nonexistent_pizza_is_refused` |
| C4 Token | the user's own (base) | from auth | `test_base_choice_is_saved` |
| C4 Token | none | no header | `test_rating_without_token_is_refused` |
| C4 Token | wrong length | token short | `test_rating_with_short_token_is_refused` |