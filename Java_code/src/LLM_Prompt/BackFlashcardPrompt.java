package LLM_Prompt;

public class BackFlashcardPrompt {
    private String id;
    public BackFlashcardPrompt(String id){
        this.id=id;
    }
    private static boolean isInvalid(String str) {
        return str == null || str.trim().isEmpty();
    }

    public String prompt(String tag, String front, String responseLanguage) {
        // combine all tags into a single string, in the form of "tag1, tag2, tag3,..."
        if (isInvalid(tag)) {
            throw new IllegalArgumentException("Topic must not be null, empty, or blank.");
        }

        return String.format(
"We are now working on a set of flashcards learning based on examples and usages."+
" Write the back face for a flashcard whose front face is %s, and its tags: %s by starting with the term,"+ 
"%s written on a single line, then definition (and notice if applicable), "+
"and then a range of examples that cover its various use cases, while analyzing the examples. "+
"Answer strictly in %s. Your output will be threw fully into the flashcard.",
                front.trim(), tag.trim(), front.trim(), responseLanguage.trim()
        );
    }
}


// "Provided that I am a learner dealing with flashcards. " +
//                         "I want to write a flashcard's back face from its front face, %s, " +
//                         "and its tags: %s (representing language, field of study, type, etc.). " +
//                         "Give me detailed information about anything I need to learn about %s, " +
//                         "including a wide range of examples that cover its various use cases. " +
//                         "Answer strictly in %s. Your output will be threw fully into the flashcard, " +
//                         "so please do not start or end with any irrelevant sentences. " +
//                         "Start your response exactly with what is on the front face.",