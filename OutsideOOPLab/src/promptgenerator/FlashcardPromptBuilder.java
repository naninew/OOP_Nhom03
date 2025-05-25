package promptgenerator;

public class FlashcardPromptBuilder {
	private static boolean isInvalid(String str) {
        return str == null || str.trim().isEmpty();
    }

    public static String buildPrompt(String topic, String term, String responseLanguage, String userLanguage) {
        if (isInvalid(topic)) {
            System.out.println("Topic must not be null, empty, or blank.");
        } // suppose this doesn't happen, and according to the database, 
          // responseLanguage and term cannot be null, so we do not need
          // to work on handling them.

        String result = String.format(
            "Provided that I am a learner of %s dealing with flashcards. " +
            "I want to write a flashcard's back face from its front face, %s. " +
            "Give me detailed information about anything I need to learn about %s, " +
            "including a wide range of examples that cover its various use cases. " +
            "Answer strictly in %s. Your output will be threw fully into the flashcard, " +
            "so please do not start or end with any irrelevant sentences.",
            topic.trim(), term.trim(), term.trim(), responseLanguage.trim()
        );
        
        return result;
    }
}