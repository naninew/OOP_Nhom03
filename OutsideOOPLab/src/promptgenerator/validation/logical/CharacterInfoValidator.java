package promptgenerator.validation.logical;

import promptgenerator.validation.*;
import promptgenerator.model.*;

public class CharacterInfoValidator implements LogicalValidator<ChineseCharacterInfo> {
    public ValidationResult validate(ChineseCharacterInfo characterInfo) {
        ValidationResult result = new ValidationResult();
        if (characterInfo.getCharacter() == null || characterInfo.getCharacter().isEmpty()) {
            result.addError("Character cannot be empty.");
        }
        return result;
    }
}
