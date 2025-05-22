package promptgenerator.validation.semantic;

import promptgenerator.core.*;
import promptgenerator.model.*;
import promptgenerator.validation.*;

public class SemanticValidationBuilder {

    public ValidationResult build(PromptContext context) {
        Object input = context.getInput();

        if (input instanceof WordInfo) {
            return new WordInfoHintsGenerator(context).validate((WordInfo) input);
        } else if (input instanceof ChineseCharacterInfo) {
            return new CharacterInfoHintsGenerator(context).validate((ChineseCharacterInfo) input);
        } else if (input instanceof RadicalInfo) {
            return new RadicalInfoHintsGenerator(context).validate((RadicalInfo) input);
        } 
        // Add more as needed later
        else {
            return new ValidationResult(); // empty
        }
    }
}
