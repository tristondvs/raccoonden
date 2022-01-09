#include <iostream>
#include <string>
#include <thread> // standard C++11

// function to output as if it was being typed
void type_text(const std::string& text)
{
    // loop through each character in the text
    for (std::size_t i = 0; i < text.size(); ++i)
    {
        // output one character
        // flush to make sure the output is not delayed
        std::cout << text[i] << std::flush;

        // sleep 60 milliseconds
        std::this_thread::sleep_for(std::chrono::milliseconds(30));
    }
}

int main() {
std::string player;
std::string anykey;
std::string choice1;
// title of game big letters: MANIFEST
std::cout << "________________________________________________\n";
std::cout << "================================================\n";
std::cout << "MM MM   A   N    N IIIII FFFFF EEEEE  SSSS TTTTT\n";
std::cout << "MM MM A   A N N  N   I   F     E     SS      T  \n";
std::cout << "M M M AAAAA N  N N   I   FFF   EEE     SS    T  \n";
std::cout << "M   M A   A N    N IIIII F     EEEEE SSSSS   T  \n";
std::cout << "================================================\n";
std::cout << "________________________________________________\n";
std::cout << "                   Manifest!                     \n";
// enter your name, intro
std::cout << "Please enter your name: \n";
std::cin >> player;
std::cout << "\n\n" << "Welcome to Manifest, " << player << "\n";
std::cout << "Before you lay a series of trials as you create your story in this world. Your choices will choose the path you will take to complete your adventure. \n\n";
std::cout << "Be wary, some choices will lead you into inescapable doom and end your adventure immediately, while other choices will prolong your journey. \n\n";
std::cout << "Press any key, and then hit ENTER/RETURN to continue: \n";
std::cin >> anykey;
// wake up on beach
type_text("You hear the sound of waves softly crashing as water runs up your leather leguards and to your stomach. You open your eyes and wince; the bright light cuts into your eyes and your head begins to throb... Your hand moves to cover your eyes and knocks a small tuff of sand into your face. You try to recall the events that led you to the shoreline while patting the sand away from your lips...\n\n");
type_text("*...What happened?*, you thought to yourself, almost as if to warrant a quick explanation for this mess you have found yourself in. Your eyes slowly begin to adjust to the sun, and you see pieces of wooden planks scattered around you on the shoreline.\n\n");

// conditional to gather info about surroundings
int advance1 = 0;
while (advance1 < 3) {
std::cout << "Which direction would you like to look, " << player <<"? Enter your choice below. \n\n";
std::cout << "- front \n";
std::cout << "- left \n";
std::cout << "- behind \n";
std::cout << "- right \n";
std::cout << "- nowhere\n";
std::cin >> choice1;
if (choice1 == "behind") {
    type_text("The ocean stretches out before you as far as you can see, as the sun sits high into the sky. The sea looks somewhat calm, causing you to wonder how long you must have been passed out on the shore.\n");
    advance1++;
}
else if (choice1 == "left") {
    type_text("The shoreline seems to strech out for at least 300 yards, and then tuck its way towards land. This must be some sort of island.\n");
    advance1++;
}
else if (choice1 == "front") {
    type_text("In front of you rests a lush jungle. Further into the distance you can see a pillar of smoke rising against a clear, blue sky.\n\n");
    type_text("*At least I am not alone,* you muttered to yourself, as you let out a sigh of relief, *Maybe there is someone near that source of smoke that can give me some insight as to where I am.* \n");
    advance1++;
}
else if (choice1 == "right") {
    type_text("In the distance, you can see what looks to be an aging tower. There is an opening at the top that appears to serve as a lookout. Maybe you can get a better view of the area from there. \n");
    advance1++;
}
else if (choice1 == "nowhere" && advance1 < 2) {
    type_text("I don't have any more time for looking around, you say to yourself. However, you realize that you still don't have a proper lay of the land yet. Perhaps you should look around a bit more.");
    }
else if (choice1 == "nowhere" && advance1 >= 2) {
    type_text("You feel like you have a pretty good understanding of where you might be able to get some help. It is probably best to get a move on before nightfall.\n\n");
    }
else {
    std::cout << "\n Choose one of the available options to continue. Hint: type left and hit ENTER to look left. \n\n";
}

// head into woods
// walk into town
// tower over ocean
// wait

}
}
