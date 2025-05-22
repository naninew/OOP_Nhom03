package promptgenerator.core;

import promptgenerator.model.*;
import promptgenerator.validation.ValidationResult;
import promptgenerator.validation.logical.*;
import promptgenerator.validation.semantic.*;

public class PromptValidator {
    public ValidationResult validate(PromptContext context) {
        ValidationResult result = new ValidationResult();

        // 1. Logical validation
        if (context.getInput() != null) {
        	if (context.getInput() instanceof WordInfo) {
        		LogicalValidator<WordInfo> wordValidator = new WordInfoValidator();
                result.merge(wordValidator.validate((WordInfo)context.getInput()));
        	}
        	else if (context.getInput() instanceof ChineseCharacterInfo) {
        		LogicalValidator<ChineseCharacterInfo> characterValidator = new CharacterInfoValidator();
                result.merge(characterValidator.validate((ChineseCharacterInfo)context.getInput()));
        	}
        	else if (context.getInput() instanceof RadicalInfo) {
        		LogicalValidator<RadicalInfo> radicalValidator = new RadicalInfoValidator();
                result.merge(radicalValidator.validate((RadicalInfo)context.getInput()));
        	}
        }
        // 2. Semantic hints (as prompt modules)
        if (context.isIncludeValidationHints()) {
            SemanticValidationBuilder hintBuilder = new SemanticValidationBuilder();
            result.setHints(hintBuilder.build(context).getHints());
        }

        return result;
    }
}
