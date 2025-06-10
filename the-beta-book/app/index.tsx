import { Image } from 'expo-image';
import React from 'react';
import { Dimensions, StyleSheet, Button, View, ScrollView, Text, Alert} from 'react-native';


import { Collapsible } from '@/components/Collapsible';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

const Separator = () => <View style={styles.separator} />;

export default function Index() {
  return (
    <View style={styles.container}>
      <View style={styles.searchbar}>
        <ThemedText>
          Search Bar
        </ThemedText>
      </View>
      
      <Separator />

      <ScrollView>
        <Collapsible title="Climb 1">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>

        <Separator />

        <Collapsible title="Climb 2">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>
        
        <Separator />

        <Collapsible title="Climb 3">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>
        
        <Separator />

        <Collapsible title="Climb 4">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>
        
        <Separator />

        <Collapsible title="Climb 5">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>
        
        <Separator />

        <Collapsible title="Climb 6">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>
        
        <Separator />

        <Collapsible title="Climb 7">
          <ThemedText>
            Climbing info and images and stuff
          </ThemedText>
        </Collapsible>

      </ScrollView>
    </View>
  );
}

const searchbarHeight = Dimensions.get('window').height / 18;
const separatorHeight = Dimensions.get('window').height / 20;

const styles = StyleSheet.create({
  searchbar: {
    textAlign: 'center',
    height: searchbarHeight,
  },
  container: {
      margin:10,
      overflow:'hidden'
  },
  title: {
    textAlign: 'center',
    marginVertical: 8,
  },
  separator: {
    height: separatorHeight,
  },
});