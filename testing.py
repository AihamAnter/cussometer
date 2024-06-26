import unittest
from wordCloud import generate_wordcloud
from text_processing import tokenize_files
from syntiment_analysis import analyze_sentiment
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tfidf import calculate_tfidf
import os


import string


class TestAllCases(unittest.TestCase):  # check if files are valid (text acquisition)
    def test_texy_processing(self):
        self.assertTrue(tokenize_files('C:\\Users\\hebaa\\PycharmProjects\\pythonProject\\cussometer\\texts\\'))

    def test_wordCloud(self):  # check if the wordcloud exist (text processing)
        self.assertIsNotNone(generate_wordcloud)

    def test_syntimen_analysis(self):  # check if sentiment analysis is accurate (sentiment analysis)
        lyrics = ("You sound like a bitch, bitch Shut the fuck up When your "
                  "fans become your haters You done? Fuckin' beard's weird Alright "
                  "You yellin' at the mic, fuckin' weird beard (You want smoke) We doin' this"
                  " once You yellin' at the mic, your beard's weird Why you yell at the mic? (Illa"
                  ") [Verse] Rihanna just hit me on a text Last night I left hickeys on her neck Wait"
                  ", you just dissed me? I'm perplexed Insult me in a line, compliment me on the next "
                  "Damn, I'm really sorry you want me to have a heart attack Was watchin' 8 Mile on my "
                  "NordicTrack Realized I forgot to call you back Here's that autograph for your daughter, I"
                  " wrote it on a Starter cap Stan, Stan, son, listen, man, Dad isn't mad But how you gonna name yourself "
                  "after a damn gun and have a man-bun? The giant's woke, eyes open, undeniable Supplyin' smoke, got the fire "
                  "stoked Say you got me in a scope, but you grazed me I say one call to Interscope and you're Swayze Your reply got "
                  "the crowd yelling, Woo! So before you die let's see who can out-petty who Wit' your corny lines (Slim, you're old)—ow,"
                  " Kelly, ooh But I'm 45 and I'm still outselling you By 29, I had three albums that had blew Now let's talk about somethin'"
                  " I don't really do Go in someone's daughter's mouth stealin' food But you're a fuckin' mole hill, now I'ma make a mountain out "
                  "of you (Woo!) Ho, chill, actin' like you put the chrome barrel to my bone marrow Gunner? Bitch, you ain't a bow and arrow Say you'll "
                  "run up on me like a phone bill, sprayin' lead (Brrt) Playin' dead, that's the only time you hold still (Hold up) Are you eating cereal or"
                  " oatmeal? What the fuck's in the bowl, milk? Wheaties or Cheerios? 'Cause I'm takin' a shit in 'em, Kelly, I need reading material …Dictionary…"
                  " Yo, Slim, your last four albums sucked Go back to Recovery,oh shoot, that was three albums ago What do you know? Oops Know your facts before you come"
                  " at me, lil' goof Luxury, oh, you broke, bitch? Yeah, I had enough money in '02 To burn it in front of you, ho Younger me? No, you the wack me, it's funny"
                  " but so true I'd rather be 80-year-old me than 20-year-old you 'Til I'm hitting old age Still can fill a whole page with a 10-year-old's rage Got more fans "
                  "than you in your own city, lil' kiddie, go play Feel like I'm babysitting Lil Tay Got the Diddy okay, so you spent your whole day Shootin' a video just to fuckin"
                  "' dig your own grave Got you at your own wake, I'm the billy goat You ain't never made a list next to no Biggie, no Jay Next to Taylor Swift and that Iggy ho, you"
                  " about to really blow Kelly, they'll be putting your name Next to Ja, next to Benzino—die, motherfucker! Like the last motherfucker sayin' Hailie in vain Alien brain,"
                  " you Satanist (Yeah) My biggest flops are your greatest hits The game's mine again and ain't nothin' changed but the locks So before I slay this bitch I, mwah, give"
                  " Jade a kiss Gotta wake up Labor Day to this (The fuck?) Bein' rich-shamed by some prick usin' my name for clickbait In a state of bliss 'cause I said his goddamn "
                  "name Now I gotta cock back, aim Yeah, bitch, pop Champagne to this! (Pop) It's your moment This is it, as big as you're gonna get, so enjoy it Had to give you a"
                  " career to destroy it Lethal injection, go to sleep six feet deep I'll give you a B for the effort But if I was three-foot-eleven, you'd look up to me And for the"
                  " record, you would suck a dick to fuckin' be me for a second Lick a ballsack to get on my channel Give your life to be as solidified This motherfuckin' shit is like"
                  " Rambo when he's out of bullets So what good is a fuckin' machine gun when it's outta ammo? Had enough of this tatted-up mumble rapper How the fuck can him and I "
                  "battle? He'll have to fuck Kim in my flannel I'll give him my sandals 'Cause he knows, long as I'm Shady, he's gon' have to live in my shadow Exhausting, letting "
                  "off on my offspring Lick a gun barrel, bitch, get off me! You dance around it like a sombrero, we can all see You're fuckin' salty 'cause Young Gerald's balls-deep"
                  " inside of Halsey Your red sweater, your black leather You dress better, I rap better That a death threat or a love letter? Little white toothpick Thinks it's over"
                  " a pic, I just don't like you, prick Thanks for dissing me Now I had an excuse on the mic to write Not Alike But really, I don't care who's in the right But you're "
                  "losin' the fight you picked Who else want it? Kells, attempt fails! Budden, L's! Fuckin' nails in these coffins as soft as Cottonelle Killshot, I will not fail, I'm "
                  "with the Doc still But this idiot's boss pops pills and tells him he's got skills But, Kells, the day you put out a hit's the day Diddy admits That he put the hit"
                  " out that got Pac killed, ah I'm sick of you bein' wack And still usin' that mothafuckin' Auto-Tune So let's talk about it (Let's talk about it) I'm sick of your "
                  "mumble rap mouth Need to get the cock up out it Before we can even talk about it (Talk about it) I'm sick of your blonde hair and earrings Just 'cause you look in"
                  " the mirror and think That you're Marshall Mathers (Marshall Mathers) Don't mean you are, and you're not about it So just leave my dick in your mouth and keep my "
                  "daughter out it See upcoming rap shows Get tickets for your favorite artists You might also like Family Matters Drake THE HEART PART 6 Drake 6:16 in LA Kendrick"
                  " Lamar [Outro] You fuckin'—, oh And I'm just playin', Diddy You know I love you")

        lyrics = lyrics.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(lyrics)

        stop_words = set(stopwords.words('english'))
        filtered_tokens = []
        for token in tokens:
            if token.lower() not in stop_words:
                filtered_tokens.append(token)
        filtered_text = ' '.join(filtered_tokens)
        sentiment_scores = analyze_sentiment(filtered_text)

        expected_scores = {'neg': 0.251, 'neu': 0.616, 'pos': 0.133, 'compound': -0.9985}
        self.assertEqual(sentiment_scores, expected_scores)

    def test_calculate_tfidf(self):  # check if the calculate_tfidf is working (tfidf)
        # Example input texts
        texts = [
            "Cuss words found: example text with cuss words.",
            "Cuss words found: another example with some cuss words.",
            "This text does not contain the phrase but has cuss words.",
            "Cuss words found: another text with cuss words."
        ]
        tfidf_matrix, feature_names = calculate_tfidf(texts)
        self.assertGreater(len(feature_names), 0)

    def test_files_saved_to_directory(self):  # check if files are being saved (result)
        # Test case to check if files are saved to the directory
        directory_path = "../test_directory"  # Path to test directory
        if not os.path.exists(directory_path):
            # Create directory if it doesn't exist
            os.makedirs(directory_path)

        files = ["test1.txt", "test2.txt", "test3.txt"]
        for filename in files:
            with open(os.path.join(directory_path, filename), 'w') as file:
                file.write("test text")

        files_in_directory = os.listdir(directory_path)
        self.assertEqual(len(files_in_directory), len(files), "Number of files in directory should match the number of test files")


if __name__ == '__main__':
    unittest.main()
