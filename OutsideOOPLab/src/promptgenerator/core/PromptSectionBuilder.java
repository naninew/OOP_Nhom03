package promptgenerator.core;

import promptgenerator.vocabulary.*;
import promptgenerator.chinesecharacter.*;
import promptgenerator.model.*;
import java.util.*;

public class PromptSectionBuilder {

    public String build(PromptContext context) {
        StringBuilder result = new StringBuilder();
        for (PromptPart part : context.getIncludedParts()) {
            String section = generateSection(part, context);
            if (section != null && !section.isEmpty()) {
                result.append(section).append("\n\n");
            }
        }
        return result.toString().trim();
    }

    private String generateSection(PromptPart part, PromptContext context) {
        switch (part) {
            case DEFINITION:
                return new DefinitionPrompt().generate(context.getInput());
            case USAGE:
                return new UsagePrompt().generate(context.getInput());
            case EXAMPLES:
                return new CharacterExamplePrompt().generate(context.getInput());
            case SYNONYMS:
                return new SynonymComparisonPrompt().generate(context.getInput());
            case CONFUSED_TERMS:
                return new ConfusedWordsPrompt().generate(context.getInput());
            case RADICALS_ANALYSIS:
                return new RadicalAnalysisPrompt().generate(context.getInput());
            case READINGS:
                return new ReadingsPrompt().generate(context.getInput());
            case RELATED_TERMS:
                return new RelatedCharactersPrompt().generate(context.getInput());
            default:
                return "";
        }
    }
}
