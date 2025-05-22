package promptgenerator.core;

import promptgenerator.vocabulary.*;
import promptgenerator.chinesecharacter.*;
import promptgenerator.model.*;
import java.util.*;

public class PromptSectionBuilder {

    public String build(PromptContext context) {
        StringBuilder result = new StringBuilder();
        for (PromptPart part : context.getIncludedParts()) {
            String section = generateSection(context);
            if (section != null && !section.isEmpty()) {
                result.append(section).append("\n\n");
            }
        }
        return result.toString().trim();
    }

    private String generateSection(PromptContext context) {
        return " "; //temporary
    }
}
