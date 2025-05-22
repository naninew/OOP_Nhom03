package promptgenerator.validation.wip_semantic;

import java.util.*;

import promptgenerator.core.*;
import promptgenerator.model.*;

public class WordInfoHintsGenerator extends BaseValidationHintsGenerator<WordInfo> {
    public WordInfoHintsGenerator(PromptContext context) {
        super(context);
    }

    @Override
    protected List<String> checkInferableFields(WordInfo word) {
        List<String> hints = new ArrayList<>();
        if (word.getWordLevel() == null) {
            hints.add("The level is missing. Suggest the most likely level.");
        }
        if (word.getWordTypes() == null || word.getWordTypes().isEmpty()) {
            hints.add("The word type is missing. Find them.");
        }
        return hints;
    }
    
    protected List<String> checkInconsistencies(WordInfo word) {
        List<String> hints = new ArrayList<>();

        if (true) {
            hints.add(ValidationHintFragments.checkInconsistenciesFragment("word"));
        }

        return hints;
    }

    protected List<String> checkSpellingOrStandardForm(WordInfo word) {
        List<String> hints = new ArrayList<>();

        if (true) {
            hints.add(ValidationHintFragments.spellingOrNonStandardFragment("word"));
        }

        return hints;
    }
}
