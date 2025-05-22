package promptgenerator.validation.logical;

import promptgenerator.validation.ValidationResult;
import promptgenerator.validation.logical.*;
import promptgenerator.model.*;

import java.util.*;

public class LogicalValidatorTest {
    public static void main(String[] args) {
        // --- Test: ChineseCharacterInfo logical validation ---
        List<String> radicals = new ArrayList<>();
        radicals.add("走");

        ChineseCharacterInfo character1 = new ChineseCharacterInfo(
                "", "JLPT N4", radicals);

        CharacterInfoValidator characterValidator = new CharacterInfoValidator();
        ValidationResult characterValidationResult = characterValidator.validate(character1);
        System.out.println("[Character1 Validation]\n" + characterValidationResult.toText());

        // --- Test: WordInfo logical validation ---
        List<String> wordTypes = new ArrayList<>();
        wordTypes.add("noun");
        wordTypes.add("verb");

        WordInfo word1 = new WordInfo(
                "", "", "CEFR A2", wordTypes);

        WordInfo word2 = new WordInfo(
                "勉強", "", "JLPT N5", wordTypes);

        WordInfoValidator wordValidator = new WordInfoValidator();

        ValidationResult word1ValidationResult = wordValidator.validate(word1);
        System.out.println("[Word1 Validation]\n" + word1ValidationResult.toText());

        ValidationResult word2ValidationResult = wordValidator.validate(word2);
        System.out.println("[Word2 Validation]\n" + word2ValidationResult.toText());
    }
}
