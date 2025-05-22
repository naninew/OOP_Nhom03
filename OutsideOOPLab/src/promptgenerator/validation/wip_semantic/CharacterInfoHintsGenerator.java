package promptgenerator.validation.wip_semantic;

import java.util.*;

import promptgenerator.core.*;
import promptgenerator.model.*;

public class CharacterInfoHintsGenerator extends BaseValidationHintsGenerator<ChineseCharacterInfo> {
    public CharacterInfoHintsGenerator(PromptContext context) {
        super(context);
    }

    @Override
    protected List<String> checkInferableFields(ChineseCharacterInfo character) {
        List<String> hints = new ArrayList<>();
        if (character.getRadicals() == null || character.getRadicals().isEmpty()) {
            hints.add("The radicals are missing. Find which radicals this character belongs to.");
        }
        if (character.getCharacterLevel() == null) {
            hints.add("The level is missing. Suggest the level of Japanese this character belongs to.");
        }
        return hints;
    }
    
    protected List<String> checkInconsistencies(ChineseCharacterInfo character) {
        List<String> hints = new ArrayList<>();

        // Placeholder for actual logic (e.g., reading type mismatch, missing radicals)
        if (true) {
            hints.add(ValidationHintFragments.checkInconsistenciesFragment("Chinese character"));
        }

        return hints;
    }

    protected List<String> checkSpellingOrStandardForm(ChineseCharacterInfo character) {
        List<String> hints = new ArrayList<>();

        if (true) {
            hints.add(ValidationHintFragments.spellingOrNonStandardFragment("Chinese character"));
        }

        return hints;
    }

}
