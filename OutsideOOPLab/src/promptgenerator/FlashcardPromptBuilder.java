package promptgenerator;

public class FlashcardPromptBuilder {
	private static boolean isInvalid(String str) {
        return str == null || str.trim().isEmpty();
    }

    public static String buildPrompt(String topic, String term, String responseLanguage) {
        if (isInvalid(topic)) {
            throw new IllegalArgumentException("Topic must not be null, empty, or blank.");
        }
        if (isInvalid(term)) {
            throw new IllegalArgumentException("Term must not be null, empty, or blank.");
        }
        if (isInvalid(responseLanguage)) {
            throw new IllegalArgumentException("Response language must not be null, empty, or blank.");
        }

        return String.format(
            "Provided that I am a learner of %s dealing with flashcards. " +
            "I want to write a flashcard's back face from its front face, %s. " +
            "Give me detailed information about anything I need to learn about %s, " +
            "including a wide range of examples that cover its various use cases. " +
            "Answer strictly in %s. Your output will be threw fully into the flashcard, " +
            "so please do not start or end with any irrelevant sentences.",
            topic.trim(), term.trim(), term.trim(), responseLanguage.trim()
        );
    }
}