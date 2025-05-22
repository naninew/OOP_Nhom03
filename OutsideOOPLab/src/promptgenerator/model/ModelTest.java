package promptgenerator.model;

import java.util.*;

public class ModelTest {
	public static void main(String[] args) {
		//test kanji---------------------------------------------
		
		List<String> radicals = new ArrayList<>();
		String radical1 = "走";
		radicals.add(radical1);
		
		ChineseCharacterInfo character1 = new ChineseCharacterInfo(
				"走", "JLPT N4", radicals);
		
		System.out.println(character1.toText());
		
		//test word---------------------------------------------
		
		List<String> wordTypes = new ArrayList<>();
		String wordType1 = "noun";
		String wordType2 = "verb";
		wordTypes.add(wordType1);
		wordTypes.add(wordType2);
		
		WordInfo word1 = new WordInfo(
				"record", "English", "CEFR A2", wordTypes);
		
		WordInfo word2 = new WordInfo(
				"勉強", "Japanese", "JLPT N5", wordTypes);
		
		System.out.println(word1.toText());
		System.out.println(word2.toText());
	}
}
