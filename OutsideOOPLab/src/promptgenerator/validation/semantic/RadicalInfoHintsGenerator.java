package promptgenerator.validation.semantic;

import java.util.*;

import promptgenerator.core.*;
import promptgenerator.model.*;

public class RadicalInfoHintsGenerator extends BaseValidationHintsGenerator<RadicalInfo> {
    public RadicalInfoHintsGenerator(PromptContext context) {
        super(context);
    }

    @Override
    protected List<String> checkInferableFields(RadicalInfo radical) {
        List<String> hints = new ArrayList<>();
        if (radical.getOriginalCharacter() == null) {
            hints.add("The original character is missing. Find which character this radical comes from.");
        }
        return hints;
    }
    
    protected List<String> checkInconsistencies(RadicalInfo radical) {
        List<String> hints = new ArrayList<>();

        if (true) {
            hints.add(ValidationHintFragments.checkInconsistenciesFragment("radical"));
        }

        return hints;
    }

    protected List<String> checkSpellingOrStandardForm(RadicalInfo radical) {
        List<String> hints = new ArrayList<>();

        if (true) {
            hints.add(ValidationHintFragments.spellingOrNonStandardFragment("radical"));
        }

        return hints;
    }
}
