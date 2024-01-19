# Entertainment Recommendation Software

*(This project was created as part of an assignment for the Computer Science Career Path from Codecademy.com)*

Entertainment Recommendation Software (ERS) is a recommendation system which takes the characteristics you value most about your media and turns them into a list of suitable media for you to consume. 

## Usage
To use the software, run the `script.py` file and follow the given prompts: 
 1) First, you will either select a form of media that you would like to focus on (games, movies, tv shows, or songs), or a metric by which you want to narrow down your choices (release date, genre, or length). 
 2) Depending on what you chose in step one, one of a couple things could happen: 
    - If you selected a media type, then you will now be prompted to select a metric to narrow down your choices further. 
    - If you were unsure of which media type you wanted at step one, you also had the option to focus solely on the other metrics. By choosing "Not sure", you basically just skip to the next step. 
        - Note: This will result in a collection of recommendations for *all* of the media types.
3) One final round of questions! Once you've narrowed down which metric you want to select your media based on, all you need to do is choose which side of the options you want to focus on. 
    - For example, if you chose to focus on the release date, the final step would be to hone in on either the oldest titles or the most recent. 

And that's it! You now have a small collection of media to choose from that fits your general specifications.

As new media is cycled through the system, new recommendations may appear for the same queries. Come back periodically to see what's new!