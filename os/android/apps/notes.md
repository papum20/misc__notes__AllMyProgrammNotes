# NOTES

## navigation

tp get navigation controller, using in `xml` `<androidx.fragment.app.FragmentContainerView>` :
*	```kotlin
	val navHostFragment = supportFragmentManager.findFragmentById(R.id.fragment_nav_container) as NavHostFragment
	val navController = navHostFragment.navController
	```
	*	ref: https://stackoverflow.com/questions/50502269/illegalstateexception-link-does-not-have-a-navcontroller-set
*	and this is the recommended way by google, not the simple `fragment`

To use navigation (graph) with bottomNavBar :
*	menu entries ids must be the same as the destination ids
*	then use `bottomNavBar.setupWithNavController(navController)`, no need for `onNavigationItemSelected` listener

## OpenCV
Making opencv work in android studio is tricky, especially with kotlin.

steps:
1.	download opencv sdk from website in any location
2.	from android studio, do `File -> New -> Import Module` and select the opencv sdk folder - it will be copied in your project root dir
3.	edit the following files :
	*	`opencv/build.gradle.kts` :
		```kotlin
		plugins {
			id("com.android.library")
			id("maven-publish")
			id("kotlin-android")
			id("org.jetbrains.kotlin.android")	//version "1.7.10"	//version may differ for your setup
		}

		val openCVersionName = "4.9.0"
		val openCVersionCode = ((4 * 100 + 9) * 100 + 0) * 10 + 0

		println("OpenCV: $openCVersionName ${project.buildscript.sourceFile}")

		android {
			namespace = "org.opencv"
			compileSdk = 31
			//compileSdkVersion = 31

			defaultConfig {
				minSdk = 21
				/*
				minSdkVersion 21
				targetSdkVersion 31

				versionCode = openCVersionCode
				versionName = openCVersionName
				*/

				externalNativeBuild {
					cmake {
						arguments("-DANDROID_STL=c++_shared")
						targets("opencv_jni_shared")
					}
				}
			}

			compileOptions {
				sourceCompatibility = JavaVersion.VERSION_17	//JavaVersion.VERSION_1_8
				targetCompatibility = JavaVersion.VERSION_17	//JavaVersion.VERSION_1_8
			}

			buildTypes {
				getByName("debug") {
					packagingOptions {
						doNotStrip("**/*.so") // controlled by OpenCV CMake scripts
					}
				}
				getByName("release") {
					packagingOptions {
						doNotStrip("**/*.so") // controlled by OpenCV CMake scripts
					}
					/*
					minifyEnabled(false)
					*/
					proguardFiles(getDefaultProguardFile("proguard-android.txt"), "proguard-rules.txt")
				}
			}

			buildFeatures {
				aidl = true
				prefabPublishing = true
				//OpenCV project uses buildConfig feature. Please enable it in MyApplication/OpenCV/build.gradle file to android block:
				buildConfig = true
			}
			/*
			prefab {
				named("opencv_jni_shared") {
					headers("native/jni/include")
				}
			}
			*/

			sourceSets {
				getByName("main") {
					jniLibs.srcDirs("native/libs")
					java.srcDirs("java/src")
					aidl.srcDirs("java/src")
					res.srcDirs("java/res")
					manifest.srcFile("java/AndroidManifest.xml")
				}
			}

			/*
			publishing {
				singleVariant("release") {
					withSourcesJar()
					withJavadocJar()
				}
			}
			*/

			externalNativeBuild {
				cmake {
					path(project.projectDir.toString() + "/libcxx_helper/CMakeLists.txt")
				}
			}
		}

		/*
		publishing {
			publications {
				create<MavenPublication>("release") {
					groupId = "org.opencv"
					artifactId = "opencv"
					version = "4.9.0"

					afterEvaluate {
						from(components.release)
					}
				}
			}
			repositories {
				maven {
					name = "myrepo"
					url = "${project.buildDir}/repo"
				}
			}
		}
		*/

		dependencies {
		}
		```
		*	note: make the sdk versions match your project's
	*	`settings.gradle.kts` :
		```kotlin
		val opencvsdk="opencv/"

		pluginManagement {
			repositories {
				google()
				mavenCentral()
				gradlePluginPortal()
			}
		}
		dependencyResolutionManagement {
			repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
			repositories {
				google()
				mavenCentral()
			}
		}

		rootProject.name = "Homecook's companion"
		include(":app")

		include(":opencv")
		project(":opencv").projectDir = File(opencvsdk)
		```

		`build.gradle.kts` :
		```kotlin
		// Top-level build file where you can add configuration options common to all sub-projects/modules.
		plugins {
				id("com.android.application") version "8.2.2" apply false
				id("org.jetbrains.kotlin.android") version "1.9.22" apply false
		}

		// for navigation/safeArgs
		buildscript {
				repositories {
						google()
				}
				dependencies {
						val nav_version = "2.7.7"
						classpath("androidx.navigation:navigation-safe-args-gradle-plugin:$nav_version")
				}
		}
		```
	*	`app/build.gradle.kts` :
		```kotlin
		plugins {
			id("com.android.application")
			id("org.jetbrains.kotlin.android")
				id("androidx.navigation.safeargs.kotlin")
				id("kotlin-parcelize")  // allow automatic @Parcelize (for bundles)
				kotlin("kapt")                  // Kotlin Annotation Processing Tool, for Room
		}

		android {
			namespace = "com.papum.homecookscompanion"
			compileSdk = 34

			defaultConfig {
				applicationId = "com.papum.homecookscompanion"
				minSdk = 30
				targetSdk = 34
				versionCode = 1
				versionName = "1.0"

				testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
			}

			buildTypes {
				release {
					isMinifyEnabled = false
				proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
				}
			}
			compileOptions {
				sourceCompatibility = JavaVersion.VERSION_1_8
				targetCompatibility = JavaVersion.VERSION_1_8
			}
			kotlinOptions {
				jvmTarget = "1.8"
			}
			buildFeatures {
				viewBinding = true
			}
		}

		dependencies {

				val work_version = "2.9.0"

			implementation("androidx.core:core-ktx:1.10.1")
			implementation("androidx.appcompat:appcompat:1.6.1")
			implementation("com.google.android.material:material:1.9.0")
			implementation("androidx.constraintlayout:constraintlayout:2.1.4")
			implementation("androidx.navigation:navigation-fragment-ktx:2.7.7")
			implementation("androidx.navigation:navigation-ui-ktx:2.7.7")
			implementation("androidx.room:room-ktx:2.6.1")
			testImplementation("junit:junit:4.13.2")
			androidTestImplementation("androidx.test.ext:junit:1.1.5")
			androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
			kapt("androidx.room:room-compiler:2.6.1")

				// WorkManager
				// (Java only)
				implementation("androidx.work:work-runtime:$work_version")
				// Kotlin + coroutines
				implementation("androidx.work:work-runtime-ktx:$work_version")
				// optional - RxJava2 support
				implementation("androidx.work:work-rxjava2:$work_version")
				// optional - GCMNetworkManager support
				implementation("androidx.work:work-gcm:$work_version")
				// optional - Test helpers
				androidTestImplementation("androidx.work:work-testing:$work_version")
				// optional - Multiprocess support
				implementation("androidx.work:work-multiprocess:$work_version")

				// ia vision
				implementation("com.google.android.gms:play-services-vision:20.1.3")
				implementation(fileTree("libs") {
						include("*.jar")
				})
				implementation(project(":opencv"))      // add opencv dependency

				/* google OCR (ML Kit) */
				// For bundling the model with your app:
				implementation("com.google.mlkit:text-recognition:16.0.0")                              // latin script
				//implementation("com.google.mlkit:text-recognition-chinese:16.0.0")
				//implementation("com.google.mlkit:text-recognition-devanagari:16.0.0")
				//implementation("com.google.mlkit:text-recognition-japanese:16.0.0")
				//implementation("com.google.mlkit:text-recognition-korean:16.0.0")

				// For using the model in Google Play Services:
				//implementation("com.google.android.gms:play-services-mlkit-text-recognition:19.0.0")                          // latin script
				//implementation("com.google.android.gms:play-services-mlkit-text-recognition-chinese:16.0.0")
				//implementation("com.google.android.gms:play-services-mlkit-text-recognition-devanagari:16.0.0")
				//implementation("com.google.android.gms:play-services-mlkit-text-recognition-japanese:16.0.0")
				//implementation("com.google.android.gms:play-services-mlkit-text-recognition-korean:16.0.0")

		}
		```
4.	follow the steps in the initial guide on the website to use opencv in your project scripts

## osmdroid


`osmdroid-android/osmbuild.gradle` :
*	```java
	description = 'An Android library to display OpenStreetMap views.'
	apply plugin: 'com.android.library'
	apply plugin: "maven-publish"


	android {
		namespace = "org.osmdroid"
		compileSdkVersion 34

		defaultConfig{
			targetSdkVersion  34
		}

		lintOptions {
			abortOnError false
		}
		testOptions { 
		unitTests.returnDefaultValues = true
	}
		buildTypes {
			release {
				minifyEnabled false
			}
		}
		publishing {
			singleVariant("release") {
				withSourcesJar()
				withJavadocJar()
			}
		}
	}


	import org.apache.tools.ant.filters.*
	task copyFiles(type: Copy) {
		from 'src/main/filtered/org/osmdroid'
		into 'src/main/java/org/osmdroid'
	}



	task androidSourcesJar(type: Jar) {
		from android.sourceSets.main.java.srcDirs
	}

	artifacts {
	//    archives packageReleaseJar
		archives androidSourcesJar

	}
	preBuild.dependsOn(copyFiles)
	```
*	note: important parts are sdk versions and add a `namespace` (and also removed some parts not recognized by gradle)

