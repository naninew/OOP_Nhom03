package promptgenerator.validation.wip_semantic;

public class ValidationHintFragments {

    public static String checkInconsistenciesFragment(String itemType) {
        return String.format(
            "Before responding, check if the provided %s attributes (e.g., level, type, reading, etc.) contradict each other. " +
            "If yes, state the correction first, then continue with the response based on the corrected attributes.", 
            itemType
        );
    }

    public static String spellingOrNonStandardFragment(String itemType) {
        return String.format(
            "If the given %s seems incorrect, non-standard, or misspelled in the language, suggest a more standard alternative " +
            "before continuing with the analysis.", 
            itemType
        );
    }
}
