public class RomanToInteger {
    public int romanToInt(String s) {
        
        int num_chars = s.length(); // finding number of characters in string
        char[] char_array = s.toCharArray(); // parsing into each character
        for (char t : char_array)
            System.out.println(t);

        // replacing characters with numbers in array
        for (char letter = 0; letter < num_chars; letter++){
            if (char_array[letter] == 'I'){
                char_array[letter] = 1;}
            else if (char_array[letter] == 'V'){
                char_array[letter] = 5;}
            else if (char_array[letter] == 'X'){
                char_array[letter] = 10;}
            else if (char_array[letter] == 'L'){
                char_array[letter] = 50;}
            else if (char_array[letter] == 'C'){
                char_array[letter] = 100;}
            else if (char_array[letter] == 'D'){
                char_array[letter] = 500;}
            else if (char_array[letter] == 'M'){
                char_array[letter] = 1000;}
        }
        int sum = 0;
        for (int y = 0; y < num_chars - 1; y++){
            System.out.println(y);
            if (char_array[y] < char_array[y+1]){
                sum = sum + char_array[y+1] - char_array[y];
                y = y+2;}
            else {
                sum = sum + char_array[y];
                if (y+1 == num_chars - 1){
                    sum = sum + char_array[y+1];
                }
            }
            }
        return sum;
    }
}

