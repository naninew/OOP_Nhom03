package promptgenerator.validation.logical;

import promptgenerator.validation.*;
import promptgenerator.model.*;

public class WordInfoValidator implements LogicalValidator<WordInfo> {
    public ValidationResult validate(WordInfo wordInfo) {
        ValidationResult result = new ValidationResult();
        if (wordInfo.getWord() == null || wordInfo.getWord().isEmpty()) {
            result.addError("Word cannot be empty.");
        }
        if (wordInfo.getLanguage() == null || wordInfo.getLanguage().isEmpty()) {
            result.addError("No language specified.");
        }
        return result;
    }
}
